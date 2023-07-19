from distutils.core import setup


def readme():
    """Import the README.md Markdown file and try to convert it to RST format."""
    try:
        import pypandoc
        return pypandoc.convert('README.md', 'rst')
    except(IOError, ImportError):
        with open('README.md') as readme_file:
            return readme_file.read()


setup(
    name='goemotions',
    version='0.1',
    description='Classify emotions of Reddit comments',
    long_description=readme(),
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    # Substitute <github_account> with the name of your GitHub account
    url='https://github.com/lkkcpaul/GoEmotions',
    author='Paokuan Chin',  # Substitute your name
    author_email='lkkcpaul@gmail.com',  # Substitute your email
    # license='MIT',
    packages=['goemotions'],
    install_requires=[
        'pypandoc==1.5'
    ],
)