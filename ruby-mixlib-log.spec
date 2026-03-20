#
# Conditional build:
%bcond_with	tests		# build with tests (not in gem)

%define		pkgname	mixlib-log
Summary:	Ruby mix-in for log functionality
Name:		ruby-%{pkgname}
Version:	3.2.3
Release:	1
License:	Apache v2.0
Group:		Development/Languages
Source0:	https://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	eef67df7266352021b486ef9504c83d6
URL:		https://github.com/chef/mixlib-log
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
%if %{with tests}
BuildRequires:	ruby-cucumber
BuildRequires:	ruby-rake
BuildRequires:	ruby-rspec
%endif
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
%setup -q -n %{pkgname}-%{version}

%build
%__gem_helper spec

%if %{with tests}
rspec
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
%{ruby_vendorlibdir}/mixlib/log.rb
%{ruby_vendorlibdir}/mixlib/log
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
%dir %{ruby_vendorlibdir}/mixlib
