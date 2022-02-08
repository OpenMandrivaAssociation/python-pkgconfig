# Disable useless provides ('_speedups.so' and similar)
#define __noautoprov '_.*\.so'

%define module pkgconfig

Summary:        Python module to interface with the pkg-config command line tool
Name:           python-%{module}
Version:	1.5.5
Release:	1
Group:          Development/Python
License:        MIT
URL:            https://github.com/matze/pkgconfig
Source0:        https://github.com/matze/pkgconfig/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
Source1:	setup.py
BuildRequires:	pkgconfig(python3)
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
%py3_build

%install
%py3_install
