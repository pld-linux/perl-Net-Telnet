#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	Telnet
Summary:	Net::Telnet Perl module
Summary(cs):	Modul Net::Telnet pro Perl
Summary(da):	Perlmodul Net::Telnet
Summary(de):	Net::Telnet Perl Modul
Summary(es):	M�dulo de Perl Net::Telnet
Summary(fr):	Module Perl Net::Telnet
Summary(it):	Modulo di Perl Net::Telnet
Summary(ja):	Net::Telnet Perl �⥸�塼��
Summary(ko):	Net::Telnet �� ����
Summary(nb):	Perlmodul Net::Telnet
Summary(pl):	Modu� Perla Net::Telnet
Summary(pt):	M�dulo de Perl Net::Telnet
Summary(pt_BR):	M�dulo Perl Net::Telnet
Summary(ru):	������ ��� Perl Net::Telnet
Summary(sv):	Net::Telnet Perlmodul
Summary(uk):	������ ��� Perl Net::Telnet
Summary(zh_CN):	Net::Telnet Perl ģ��
Name:		perl-Net-Telnet
Version:	3.03
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2f7d34b09d6117baefe89d44cff9d5fc
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::Telnet - interact with TELNET port or other TCP ports.

%description -l pl
Net::Telnet - wsparcie dla protoko�u TELNET.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Net/Telnet.pm
%{_mandir}/man3/*
