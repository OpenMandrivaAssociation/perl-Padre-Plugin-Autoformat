
%define realname   Padre-Plugin-Autoformat
%define version    1.1.2
%define release    %mkrel 2

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Reformat your text within Padre
Url:        http://search.cpan.org/dist/%{realname}
Source:     http://www.cpan.org/modules/by-module/Padre/%{realname}-%{version}.tar.gz
BuildRequires: perl-devel
BuildRequires: perl(Padre)
BuildRequires: perl(Test::More)
BuildRequires: perl(Text::Autoformat)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl(Module::Util)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This plugin allows one to reformat her text automatically with
Ctrl+Shift+J. It is using 'Text::Autoformat' underneath, so check this
module's pod for more information.





%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc LICENSE README Changes
%{_mandir}/man3/*
%perl_vendorlib/*


