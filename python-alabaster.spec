%global        uname alabaster
%global        sum A configurable sidebar-enabled Sphinx theme

Name:          python-alabaster
Version:       0.7.9
Release:       2%{?dist}
Summary:       %{sum}

URL:           https://pypi.python.org/pypi/alabaster
Source:        https://pypi.io/packages/source/a/%{uname}/%{uname}-%{version}.tar.gz
License:       MIT

BuildArch:      noarch

Buildrequires:  python-setuptools
Buildrequires:  python2-devel

%description
%{sum}.

%package -n python2-%{uname}
Summary:        %{sum}

%description -n python2-%{uname}
%{sum}.

%prep
%autosetup -n %{uname}-%{version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%files -n python2-%{uname}
%{python2_sitelib}/*
%doc LICENSE

%changelog
* Thu Mar 2 2017 Nicolas Hicher <nhicher@redhat.com> 0.7.9-2
- normalize spec file

* Mon Feb 27 2017 Nicolas Hicher <nhicher@redhat.com> 0.7.9-1
- initial package
