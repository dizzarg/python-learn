
import sys

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
    varspace()
