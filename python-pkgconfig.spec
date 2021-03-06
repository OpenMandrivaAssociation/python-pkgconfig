# Disable useless provides ('_speedups.so' and similar)
%define __noautoprov '_.*\.so'

%define shortname pkgconfig

Name:           python-%{shortname}
Version:	1.5.1
Release:	1
Summary:        Python module to interface with the pkg-config command line tool
Group:          Development/Python
License:        MIT
URL:            http://undefined.org/python/#simplejson
Source0:	https://files.pythonhosted.org/packages/6e/a9/ff67ef67217dfdf2aca847685fe789f82b931a6957a3deac861297585db6/pkgconfig-1.5.1.tar.gz
BuildArch:	noarch
BuildRequires:	python-distribute
BuildRequires:	python-sphinx
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python2)
BuildRequires:	python2-setuptools
%description
Python module to interface with the pkg-config command line tool

%package -n python2-%{shortname}
Summary:        Python module to interface with the pkg-config command line tool
Group:          Development/Python

%description -n python2-%{shortname}
Python module to interface with the pkg-config command line tool

%prep
%setup -q -n %{shortname}-%{version}
cp -a . %{py2dir}

%build
pushd %{py2dir}
%{__python2} setup.py build
popd
python setup.py build

%install
python setup.py install -O1 --skip-build --root %{buildroot}

pushd %{py2dir}
%{__python2} setup.py install --skip-build --root=%{buildroot}
popd

%files
%doc README.rst LICENSE
%{py_puresitedir}/*

%files -n python2-%{shortname}
%doc LICENSE
%{py2_puresitedir}/*
