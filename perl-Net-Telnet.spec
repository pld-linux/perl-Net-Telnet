%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	Telnet
Summary:	Net::Telnet perl module
Summary(pl):	Modu³ perla Net::Telnet
Name:		perl-Net-Telnet
Version:	3.02
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::Telnet - interact with TELNET port or other TCP ports.

%description -l pl
Net::Telnet - wsparcie dla protoko³u TELNET.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_sitelib}/Net/Telnet.pm
%{_mandir}/man3/*
