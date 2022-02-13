#!/usr/bin/python

mappingDL = {
    "2": ["a","b","c"],
    "3": ["d","e","f"],
    "4": ["g","h","i"],
    "5": ["j","k","l"]
}

def resolve_function(map: dict, param: str):
    ret = []
    for a in map[param[0]]:
        for b in map[param[1]]:
            ret.append(str(a)+str(b))
    return ret

resolve_lambda = lambda map,param: [str(a)+str(b) for a in map[param[0]] for b in map[param[1]]]

print(resolve_function(mappingDL, "23"))
print(resolve_lambda(mappingDL, "23"))




