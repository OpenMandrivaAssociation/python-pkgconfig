%define module pkgconfig

Summary:        Python module to interface with the pkg-config command line tool
Name:           python-%{module}
Version:	1.5.5
Release:	3
Group:          Development/Python
License:        MIT
URL:            https://github.com/matze/pkgconfig
Source0:        https://github.com/matze/pkgconfig/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
Source1:	setup.py
BuildRequires:	pkgconfig(python)
BuildRequires:  python3dist(setuptools)

BuildArch:	noarch

%description
Python module to interface with the pkg-config command line tool

%files
%doc README.rst LICENSE
%{py_puresitedir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -n %{module}-%{version}
%__cp %{SOURCE1} .

# fix version
sed -i -e 's|@VERSION@|%{version}|g' setup.py

%build
%py_build

%install
%py_install
