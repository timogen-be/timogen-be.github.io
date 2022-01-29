fields = '''
    first_seance: 1,
    ads_list: []
'''

def camel_case(name):
    return ''.join(word.title() for word in name.split('_'))

def store_getters():
    print('// getters\n'
          'const getters = {')
    for line in fields.split('\n'):
        if line.strip():
            name = line.strip().split(':')[0]
            print(f'  get{camel_case(name)}: state => {{ return state.{name}; }},')
    print('}')

def store_setters():
    print('// setters\n'
          'const mutations = {')
    for line in fields.split('\n'):
        if line.strip():
            name = line.strip().split(':')[0]
            print(f'  set{camel_case(name)}(state, value) {{ state.{name} = value; }},')
    print('}')

def vue_set_get():
    for line in fields.split('\n'):
        if line.strip():
            name = line.strip().split(':')[0]
            print(f'    {name}: {{\n'
                  f'      get() {{ return this.get{camel_case(name)}; }},\n'
                  f'      set(new_value) {{ return this.set{camel_case(name)}(new_value); }}\n'
                  f'    }},')

if __name__ == '__main__':
    store_getters()
    store_setters()
    vue_set_get()
