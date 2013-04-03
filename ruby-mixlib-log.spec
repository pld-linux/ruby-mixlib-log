%define		pkgname	mixlib-log
Summary:	Ruby mix-in for log functionality
Name:		ruby-%{pkgname}
Version:	1.4.1
Release:	1
License:	Apache v2.0
Group:		Development/Languages
URL:		http://github.com/opscode/mixlib-log
Source0:	http://gems.rubyforge.org/gems/%{pkgname}-%{version}.gem
# Source0-md5:	a5d3427b8ccfa3654954a90ee06a4776
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A gem that provides a simple mix-in for log functionality.

%package doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description doc
This package contains documentation for %{name}.

%prep
%setup -q

%if %{with tests}
# need RSpec2
rspec
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rdoc NOTICE
%{ruby_vendorlibdir}/mixlib/log.rb
%{ruby_vendorlibdir}/mixlib/log

# FIXME, who owns the dir?
%dir %{ruby_vendorlibdir}/mixlib

%if 0
%files doc
%defattr(644,root,root,755)
%endif
