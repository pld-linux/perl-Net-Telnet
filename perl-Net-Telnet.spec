%include	/usr/lib/rpm/macros.perl
Summary:	Net-Telnet perl module
Summary(pl):	Modu� perla Net-Telnet
Name:		perl-Net-Telnet
Version:	3.02
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/Net-Telnet-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net-Telnet - interact with TELNET port or other TCP ports.

%description -l pl
Net-Telnet - wsparcie dla protoko�u TELNET.

%prep
%setup -q -n Net-Telnet-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Net/Telnet.pm
%{_mandir}/man3/*
