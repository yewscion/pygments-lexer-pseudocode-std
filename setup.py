from setuptools import setup

setup(
    name="pygments-lexer-pseudotaxus",
    packages=["pygments_lexer_pseudotaxus"],
    version="2.0.1",
    description="Pygments Lexer for Pseudotaxus Pseudocode",
    author="Christopher Rodriguez",
    author_email="yewscion@gmail.com",
    url="https://git.sr.ht/~yewscion/pygments-lexer-pseudocode-std",
    entry_points="[pygments.lexers]\npseudotaxuslexer = pygments_lexer_pseudocode:PseudotaxusLexer",
    install_requires=[ "pygments" ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Topic :: Text Processing",
        "Topic :: Utilities",
    ]
)
