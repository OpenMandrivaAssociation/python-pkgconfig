%define module pkgconfig
%bcond tests 1

Name:		python-pkgconfig
Summary:	Python module to interface with the pkg-config command line tool
Version:	1.6.0
Release:	1
Group:		Development/Python
License:	MIT
URL:		https://github.com/matze/pkgconfig
Source0:	%{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(poetry-core)
%if %{with tests}
BuildRequires:	python%{pyver}dist(pytest)
%endif
Requires:	%{_bindir}/pkg-config

%description
Python module to interface with the pkg-config command line tool

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
pytest -k "not test_configure_extension"
%endif

%files
%doc README.rst
%{py_puresitedir}/%{module}
%{py_puresitedir}/%{module}-%{version}.dist-info
