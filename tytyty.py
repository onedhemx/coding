def fail(file):
        with open(file, 'a') as f:
            f.write('tytyty\n')
            print('данные добав')

fail('text.txt')
