Summary:	Show where your regex match assertion failed
Summary(pl.UTF-8):	Pokazywanie, gdzie dopasowanie wyrażenia regularnego się nie powiodło
Name:		python3-re_assert
Version:	1.1.0
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/re-assert/
Source0:	https://files.pythonhosted.org/packages/source/r/re-assert/re_assert-%{version}.tar.gz
# Source0-md5:	c948ac9a95285ab2b8048408fb70c978
URL:		https://pypi.org/project/re-assert/
BuildRequires:	python3-modules >= 1:3.6.1
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
re_assert provides a helper class to make assertions of regexes
simpler.

%description -l pl.UTF-8
re_assert dostarcza klasę pomocniczą ułatwiającą pisanie zapewnień
opartych na wyrażeniach regularnych.

%prep
%setup -q -n re_assert-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/re_assert.py
%{py3_sitescriptdir}/__pycache__/re_assert.cpython-*.py[co]
%{py3_sitescriptdir}/re_assert-%{version}-py*.egg-info
