#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	Telnet
Summary:	Net::Telnet Perl module - interact with TELNET port or other TCP ports
Summary(pl.UTF-8):	Moduł Perla Net::Telnet - komunikacja protokołem TELNET lub z innymi portami TCP
Name:		perl-Net-Telnet
Version:	3.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d2514080116c1b0fa5f96295c84538e3
URL:		http://search.cpan.org/dist/Net-Telnet/
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::Telnet allows you to make client connections to a TCP port and do
network I/O, especially to a port using the TELNET protocol.

%description -l pl.UTF-8
Net::Telnet pozwala na wykonywanie połączeń z portami TCP i
wykonywanie sieciowych operacji wejścia/wyjścia, w szczególności przy
użyciu protokołu TELNET.

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
%{_mandir}/man3/Net::Telnet.3pm*
