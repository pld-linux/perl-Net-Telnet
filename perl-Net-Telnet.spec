#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	Telnet
Summary:	Net::Telnet Perl module
Summary(cs.UTF-8):   Modul Net::Telnet pro Perl
Summary(da.UTF-8):   Perlmodul Net::Telnet
Summary(de.UTF-8):   Net::Telnet Perl Modul
Summary(es.UTF-8):   Módulo de Perl Net::Telnet
Summary(fr.UTF-8):   Module Perl Net::Telnet
Summary(it.UTF-8):   Modulo di Perl Net::Telnet
Summary(ja.UTF-8):   Net::Telnet Perl モジュール
Summary(ko.UTF-8):   Net::Telnet 펄 모줄
Summary(nb.UTF-8):   Perlmodul Net::Telnet
Summary(pl.UTF-8):   Moduł Perla Net::Telnet
Summary(pt.UTF-8):   Módulo de Perl Net::Telnet
Summary(pt_BR.UTF-8):   Módulo Perl Net::Telnet
Summary(ru.UTF-8):   Модуль для Perl Net::Telnet
Summary(sv.UTF-8):   Net::Telnet Perlmodul
Summary(uk.UTF-8):   Модуль для Perl Net::Telnet
Summary(zh_CN.UTF-8):   Net::Telnet Perl 模块
Name:		perl-Net-Telnet
Version:	3.03
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2f7d34b09d6117baefe89d44cff9d5fc
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::Telnet - interact with TELNET port or other TCP ports.

%description -l pl.UTF-8
Net::Telnet - wsparcie dla protokołu TELNET.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Net/Telnet.pm
%{_mandir}/man3/*
