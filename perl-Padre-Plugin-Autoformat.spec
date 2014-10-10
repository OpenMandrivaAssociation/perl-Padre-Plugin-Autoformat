%define upstream_name    Padre-Plugin-Autoformat
%define upstream_version 1.22

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Reformat your text within Padre
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Padre/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Module::Build::Compat)
BuildRequires:	perl(Module::Util)
BuildRequires:	perl(Padre)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Text::Autoformat)

BuildArch:	noarch

%description
This plugin allows one to reformat her text automatically with
Ctrl+Shift+J. It is using 'Text::Autoformat' underneath, so check this
module's pod for more information.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc LICENSE README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.220.0-2mdv2011.0
+ Revision: 657812
- rebuild for updated spec-helper

* Sun Dec 19 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.220.0-1mdv2011.0
+ Revision: 622950
- new version

* Mon Aug 16 2010 Jérôme Quelin <jquelin@mandriva.org> 1.2.0-1mdv2011.0
+ Revision: 570313
- update to v1.2.0

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 1.1.2-2mdv2010.0
+ Revision: 375912
- rebuild

* Wed May 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1.1.2-1mdv2010.0
+ Revision: 372462
- skipping failing tests

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 1.1.2

* Sun Mar 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.0.0-1mdv2009.1
+ Revision: 362085
- import perl-Padre-Plugin-Autoformat


* Sun Mar 29 2009 cpan2dist 1.0.0-1mdv
- initial mdv release, generated with cpan2dist

