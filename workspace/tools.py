import os 
import shutil
from typing import List

__SHEBANG__="#!/bin/bash\n"
__LOGGING__ = False

def expand_path(_input_path): 
    if '~' in _input_path: 
        _input_path = os.path.expanduser(_input_path)

    _input_path = os.path.expandvars(_input_path)
    return _input_path



class EnvPath: 
    def __init__(self, kp_json): 
        self._p = kp_json.get('path', None)
        self._k = kp_json.get('key', None)
        self._raw_links = kp_json.get('links', [])
        self._soft_links = []
        self._link_to_repo = kp_json.get('link-repo', False)
        self._repo_root = kp_json.get('repo-root', False)
        
        assert self._p is not None, "Valid path is required"
        assert self._k is not None, "Valid Env Key is required"

        self._p = expand_path(self._p)
        for _l in self._raw_links: 
            self.add_softlink_path(_l)

    def __str__(self): 
        return f'Env Path: Key[{self._k}] Path [{self._p}] Links[{"|".join(self._soft_links)}]'

    def add_softlink_path(self, target): 
        _target = expand_path(target)
        if os.path.exists(_target): 
            ## reuse the target name 
            tail= os.path.basename(self._p)
            self._soft_links.append(os.path.join(_target, tail))
        else: 
            ## trusting the config name as the name for the link
            self._soft_links.append(_target)

    def build_path(self, with_links=True): 
        if not os.path.exists(self._p):  
            os.mkdir(self._p)
        if not with_links: 
            return 
        for link_path in self._soft_links:
            if os.path.exists(link_path): 
                continue
            os.symlink(self._p, link_path)

    def is_repo_link(self): 
        return self._link_to_repo
    
    def is_repo_root(self): 
        return self._repo_root
    
    def env_key(self): 
        return self._k
    
    def env_value(self): 
        return self._p

    def as_export(self, with_newline): 
        nl = '\n' if with_newline else ''
        return f'export {self._k}="{self._p}"{nl}'
    
    def purge_existing(self): 
        if os.path.exists(self._p):
            shutil.rmtree(self._p)
        for link in self._soft_links: 
            if os.path.exists(link):
                os.remove(link)


class _Alias: 
    def __init__(self, alias_dict): 
        self.cmd = alias_dict.get('cmd', None)
        self.value = alias_dict.get('value', None)
        assert self.cmd is not None, "Cannot have None type Alias Cmd" 
        assert self.value is not None, "Cannot have None type Alias Value"

    @property
    def CommandLine(self):
        return f'alias {self.cmd}="{self.value}"'
    
    def __str__(self): 
        return self.CommandLine
        
class _EnvVar: 
    def __init__(self, env_var_dict): 
        pass
    def __str__(self): 
        return f'_Env Var -- Unimplemented'

class _Func: 
    def __init__(self, func_dict): 
        pass 
    
    def __str__(self): 
        return f'_Func Class -- Unimplemented '


class Workspace: 
    def __init__(self):
        self.dir_path : List[EnvPath] = [] 
        self.source_files: List[str] = []
        self.repo_links: List[EnvPath] = []
        self._repo_root: EnvPath = None

    def PurgeExistingKeyPaths(self): 
        for p in self.dir_path: 
            p.purge_existing()

    def AddToWorkspace(self, ep: EnvPath): 
        if ep.is_repo_link(): 
            self.repo_links.append(ep)
        else: 
            self.dir_path.append(ep)
        
        if ep.is_repo_root(): 
            self._repo_root = ep

    def BuildFileStructure(self): 
        for p in self.dir_path: 
            p.build_path()
        for p in self.repo_links: 
            if __LOGGING__: print(f'Logging {p}')

    def CacheForSummaryFile(self, input_path): 
        _p = os.path.expandvars(input_path)
        if os.path.exists(_p): 
            self.source_files.append(_p)

    def BuildGeneratedEnvFile(self, env_file_list): 
        def _write_ws_files(_n, repo_links, structure_paths): 
            if os.path.exists(_n): os.remove(_n)
            with open(_n, 'w') as export_file:
                export_file.write('\n\n## Export Paths: \n')
                exp_paths = [path.as_export(True) for path in structure_paths]
                for exp in exp_paths: export_file.write(exp)
                
                export_file.write('\n\n## Linked Paths: \n')
                exp_paths = [path.as_export(True) for path in repo_links]
                for exp in exp_paths: export_file.write(exp)
        
        for env_file in env_file_list: 
            fname = os.path.expandvars(env_file.get('name', None))
            if fname is None: 
                continue
            if env_file.get('is_ws_files', False): 
                _write_ws_files(fname, self.repo_links, self.dir_path)
                self.CacheForSummaryFile(fname)
                continue

            content_list = env_file.get('contents', None)
            if content_list is None: 
                ## File should exist but does not have any data 
                ## Worth building 
                open(fname, 'w').close()
                self.CacheForSummaryFile(fname)
                continue
            print("Extended Env Var not implemented")
            continue
            
            
    def BuildGeneratedAliases(self, alias_list):
        for alias_file in alias_list: 
            fname = os.path.expandvars(alias_file.get('name', None))
            if fname is None: 
                continue
            command_list = alias_file.get('contents', None)
            if command_list is None: 
                ## File should exist but does not have any data 
                ## Worth building 
                open(fname, 'w').close()
                self.CacheForSummaryFile(fname)
                continue
            fname_aliases = [_Alias(cmd) for cmd in command_list]
            with open(fname, 'w') as af: 
                for a in fname_aliases: 
                    af.write(f'{a.CommandLine}\n')
            self.CacheForSummaryFile(fname)

    def BuildGeneratedFunctions(self, func_list):
        for func_file in func_list: 
            fname = os.path.expandvars(func_file.get('name', None))
            if fname is None: 
                continue
            command_list = func_file.get('contents', None)
            if command_list is None: 
                ## File should exist but does not have any data 
                ## Worth building 
                open(fname, 'w').close()
                self.CacheForSummaryFile(fname)
                continue
            print("Extended Functions Not Implemented")
            continue

    def BuildJumpFile(self, summary_json): 
        _s = summary_json.get('name', None)
        _l = summary_json.get('link', None)
        assert _s is not None, 'Summary file must be real path'
        assert _l is not None, 'Link file must be real path'

        _summary_source = expand_path(_s)
        _link_summary = expand_path(_l)

        if os.path.exists(_summary_source): 
            os.path.remove(_summary_source)

        with open(_summary_source, 'w') as sf: 
            sf.write(__SHEBANG__)
            for source_file in self.source_files: 
                sf.write(f'source {source_file}\n')
        if os.path.exists(_link_summary): 
            os.remove(_link_summary)
        os.symlink(_summary_source, _link_summary)

    def BuildGeneratedJumpFile(self, summary_file): 
        _s = os.path.expandvars(summary_file)
        if os.path.exists(_s): os.path.remove(_s)
        with open(_s, 'w') as sf: 
            sf.write(__SHEBANG__)
            for source_file in self.source_files: 
                sf.write(f'source {source_file}\n')

    def CopyRepoToWorkspace(self, repo_root: str): 
        _copy_target = self._repo_root.env_value()
        if os.path.exists(_copy_target): 
            shutil.rmtree(_copy_target)
        shutil.copytree(repo_root, _copy_target)
    
    def LinkRepoDirsInWorkspace(self):  
        _root = self._repo_root.env_value()
        for _link in self.repo_links: 
            _target = _link.env_value()
            _tail = os.path.basename(_target)
            _source = os.path.join(_root, _tail)
            os.symlink(_source, _target)
        

    def __str__(self): 
        workspace_str = "Workspace: \n"
        for path in self.dir_path: 
            workspace_str += f'\t{str(path)}\n'
        return workspace_str

