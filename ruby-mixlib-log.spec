#
# Conditional build:
%bcond_without	tests		# build without tests

%define		pkgname	mixlib-log
Summary:	Ruby mix-in for log functionality
Name:		ruby-%{pkgname}
Version:	2.0.4
Release:	1
License:	Apache v2.0
Group:		Development/Languages
Source0:	https://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	fdb9b65a22703e6cef93953959545a37
URL:		https://github.com/chef/mixlib-log
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
%if %{with tests}
BuildRequires:	ruby-chefstyle
BuildRequires:	ruby-cucumber
BuildRequires:	ruby-rake
BuildRequires:	ruby-rspec < 4
BuildRequires:	ruby-rspec >= 3.7
BuildRequires:	ruby-github_changelog_generator >= 1.11.3
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
%setup -q

%build
%__gem_helper spec

%if %{with tests}
# need RSpec2
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
%doc README.rdoc NOTICE
%{ruby_vendorlibdir}/mixlib/log.rb
%{ruby_vendorlibdir}/mixlib/log
%{ruby_specdir}/%{pkgname}-%{version}.gemspec

# FIXME, who owns the dir?
%dir %{ruby_vendorlibdir}/mixlib

%if 0
%files doc
%defattr(644,root,root,755)
%endif
