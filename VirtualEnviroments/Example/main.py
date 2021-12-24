DATA = [
    {
        'name': 'Juan',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'language': 'python',
    },
]


def run():
    pythonDevs = list(
        filter(lambda worker: worker["language"] == "python", DATA))
    print(pythonDevs)


if __name__ == '__main__':
    run()
