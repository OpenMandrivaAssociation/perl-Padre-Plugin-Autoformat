%define upstream_name    Padre-Plugin-Autoformat
%define upstream_version v1.2.0

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Reformat your text within Padre
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Padre/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl(Module::Util)
BuildRequires: perl(Padre)
BuildRequires: perl(Test::More)
BuildRequires: perl(Text::Autoformat)

BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This plugin allows one to reformat her text automatically with
Ctrl+Shift+J. It is using 'Text::Autoformat' underneath, so check this
module's pod for more information.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
