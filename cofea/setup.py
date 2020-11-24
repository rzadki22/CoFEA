from setuptools import setup

setup(name='cofea',
      version='0.1',
      description="A CoFEA Initiative project",
      long_description="",
      python_requires=">=3.6",
      author='Slawomir Polanski',
      author_email='polanski.slawomir@gmail.com',
      license='TODO',
      packages=['cofea'],
      zip_safe=False,
      install_requires=[
          'jinja2',
          'pyyaml',
          'docutils>=0.15',
          'sphinx',
          'click',
          'pydata-sphinx-theme~=0.4.1',
          'beautifulsoup4',
          'importlib-resources~=3.0.0; python_version < "3.7"',
          'myst-nb', ],
      extras_require={
          "code_style": ["pre-commit~=2.7.0"],
          "sphinx": [
              "folium",
              "numpy",
              "matplotlib",
              "ipywidgets",
              "pandas",
              "nbclient"
              "myst-nb~=0.10.1",
              "sphinx-togglebutton>=0.2.1",
              "sphinx-copybutton",
              "plotly",
              "sphinxcontrib-bibtex",
              "sphinx-thebe",
              "ablog~=0.10.11"], },
      )