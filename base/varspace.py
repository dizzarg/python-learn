
import sys

def varspaceWithClass():
    n=int(sys.stdin.readline())
    class Space:
        def __init__(self, parent, name):
            self.parent = parent
            self.name = name
            self.vars = []
        
        def addVar(self, var):
            self.vars.append(var)

        def findVar(self, var):
            if var in self.vars:
                return self.name
            elif self.parent == None:
                return "None"
            else:
                return self.parent.findVar(var)
    space = {'global': Space(None, 'global')}
    for i in range(n):
        cmd, namespace, var = sys.stdin.readline().strip().split(" ")
        if cmd == 'add':
            if namespace in space:
                space[namespace].addVar(var)
            else:
                # Log error message
                # print("Parent space not exists: {}. Space: {}".format(namespace, space))
                continue
        elif cmd == 'create':
            if namespace in space:
                # Log error message
                # print("Name space exists: {}. Space: {}".format(namespace, space))
                continue
            else:
                space[namespace] = Space(space[var], namespace)
        elif cmd == 'get':
            if namespace in space:
                print("{}".format(space[namespace].findVar(var)))
            else:
                print('None')

def varspace():
    n = int(sys.stdin.readline())
    # debug info
    # print("Count {}".format(n))
    space = {'global': {"parent": None, "vars": []}}
    for i in range(n):
        cmd, namespace, var = sys.stdin.readline().strip().split(" ")
        # debug info
        # print("cmd: {}, namespace: {}, var: {}, space: {}".format(cmd, namespace, var, space))
        if cmd == 'add':
            if namespace in space:
                space[namespace]["vars"].append(var)
            else:
                # Log error message
                # print("Parent space not exists: {}. Space: {}".format(namespace, space))
                continue
        elif cmd == 'create':
            if namespace not in space and var in space:            
                space[namespace] = {"parent": var, "vars": []}
            else:
                # Log error message
                # print("Name space exists: {}. Space: {}".format(namespace, space))
                continue            
        elif cmd == 'get':        
            while True:
                if namespace not in space:
                    print("None")
                    break
                elif var in space[namespace]["vars"]:
                    print(namespace)
                    break
                else:
                    namespace = space[namespace]["parent"]

if __name__ == "__main__":
    # remove the commentary for the desired implementation
    # varspaceWithClass()    
    # varspace()
