%define module pkgconfig

Summary:        Python module to interface with the pkg-config command line tool
Name:           python-%{module}
Version:	1.5.5
Release:	4
Group:          Development/Python
License:        MIT
URL:            https://github.com/matze/pkgconfig
Source0:        https://github.com/matze/pkgconfig/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildRequires:  python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(poetry-core)

BuildArch:	noarch

%description
Python module to interface with the pkg-config command line tool

%files
%doc README.rst LICENSE
%{py_puresitedir}/*
