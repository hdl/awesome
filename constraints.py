from pathlib import Path

_root = Path(__file__).resolve().parent
_constraints = _root.parent / 'constraints'
_content = _root / 'content'

(_content / 'boards').mkdir(exist_ok=True)

for item in (_constraints / 'board').glob('**/*.yml'):

    if item.name != 'info.yml':
        _name = item.stem
        _prefix = '.todo/'
        _suffix = '.yml'
        print('·', _name)
    else:
        _name = item.parent.name
        _prefix = ''
        _suffix = ''
        print('-', _name)

    with (_content / 'boards' / (_name + '.md')).open('w') as wfptr:
        wfptr.write('---\n')
        wfptr.write(item.read_text())
        wfptr.write('ref: https://github.com/hdl/constraints/tree/main/board/%s%s%s\n' % (_prefix, _name, _suffix))
        wfptr.write('---\n')
