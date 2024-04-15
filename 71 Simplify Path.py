"""
Given a x path, which is an absolute path (starting with a slash '/') 
to a file or directory in a Unix-style file system, 
convert it to the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory, 
a double period '..' refers to the directory up a level, 
and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. 
For this problem, any other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:

    > The path starts with a single slash '/'.
    > Any two directories are separated by a single slash '/'.
    > The path does not end with a trailing '/'.
    > The path only contains the directories on the path 
      from the root directory to the target file or directory (i.e., no period '.' or double period '..')
    > Return the simplified canonical path.
"""
def simplifyPath(self, path):
    stack = []
        
    # Split the path by '/'
    components = path.split('/')
    
    for component in components:
        # Ignore empty or current directory '.'
        if component == '' or component == '.':
            continue
        
        # Handle directory up '..'
        if component == '..':
            # If stack is not empty, pop the top directory
            if stack:
                stack.pop()
        else:
            # Push valid directory names onto the stack
            stack.append(component)
    
    # Construct the simplified canonical path
    simplified_path = '/' + '/'.join(stack)
    
    return simplified_path
