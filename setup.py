from setuptools import setup

setup(
    name="pygments-lexer-pseudotaxus",
    packages=["pygments_lexer_pseudotaxus"],
    version="2.0.1",
    description="Pygments Lexer for Pseudotaxus Pseudocode",
    author="Simon Wachter",
    author_email="yewscion@gmail.com",
    url="https://git.sr.ht/~yewscion/pygments-lexer-pseudocode-std",
    license="AGPL3",
    entry_points="[pygments.lexers]\npseudotaxuslexer = pygments_lexer_pseudocode:PseudotaxusLexer",
    install_requires=[ "pygments" ],
    classifiers=[
        "Topic :: Text Processing",
        "Topic :: Utilities",
    ]
)
