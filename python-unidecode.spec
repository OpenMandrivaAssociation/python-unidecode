Summary:	ASCII transliterations of Unicode text
Name:		python-unidecode
Version:	1.3.8
Release:	1
License:	GPLv2+
Group:		Development/Python
URL:		https://pypi.org/project/unidecode/
Source0:	https://pypi.org/packages/source/U/Unidecode/Unidecode-%{version}.tar.gz

BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)

BuildArch:	noarch

%description
ASCII transliterations of Unicode text.

This is a Python port of Text::Unidecode Perl module.

%files
%{_bindir}/unidecode
%{py_sitedir}/unidecode
%{py_sitedir}/Unidecode-*.*-info

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n Unidecode-%{version}

%build
%py_build

%install
%py_install

