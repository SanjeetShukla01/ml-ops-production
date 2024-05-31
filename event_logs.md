Logs of error and warning messages:


1. SetuptoolsDeprecationWarning: setup.py install is deprecated.
While running this command `python setup.py sdist bdist_wheel` it was throwing warning message


setup.py install is deprecated.
!!

        ********************************************************************************
        Please avoid running ``setup.py`` directly.
        Instead, use pypa/build, pypa/installer or other
        standards-based tools.

        See https://blog.ganssle.io/articles/2021/10/setup-py-deprecated.html for details.
        ********************************************************************************

!!

Solution:
```
> pip install build
> python -m build
```
