#
# Conditional build:
%bcond_without	tests	# don't perform "make test"

%define		pdir	AnyData
Summary:	AnyData - easy access to data in many formats
Summary(pl.UTF-8):	AnyData - łatwy dostęp do danych w różnych formatach
Name:		perl-AnyData
Version:	0.10
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/J/JZ/JZUCKER/AnyData-%{version}.tar.gz
# Source0-md5:	ff9fb4c7d8b99d63a773e66f0ccba788
URL:		http://search.cpan.org/dist/AnyData/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-CGI
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(XML::Twig)' 'perl(HTML::TableExtract)'

%description
The AnyData modules provide simple and uniform access to data from
many sources - perl arrays, local files, remote files retrievable via
HTTP or FTP - and in many formats including flat files (CSV, Fixed
Length, Tab Delimited, etc), standard format files (Web Logs, Passwd
files, etc.), structured files (XML, HTML Tables) and binary files
with parseable headers (mp3s, jpgs, pngs, etc).

%description -l pl.UTF-8
Moduły AnyData dają prosty i ujednolicony dostęp do danych z wielu
źródeł - tablic perlowych, plików lokalnych, plików zdalnych
dostępnych po HTTP lub FTP - oraz w wielu formatach, w tym płaskich
plikach (CSV, z polami o stałej długości, ograniczonych tabami itp.),
plikach o standardowych formatach (logi WWW, pliki passwd), plikach
strukturalnych (tabele XML, HTML) oraz plikach binarnych z
parsowalnymi nagłówkami (mp3, jpg, png itp.).

%prep
%setup -q -n %{pdir}-%{version}

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
%{perl_vendorlib}/*.pm
%dir %{perl_vendorlib}/AnyData
%dir %{perl_vendorlib}/AnyData/Format
%{perl_vendorlib}/AnyData/Format/*.pm
%dir %{perl_vendorlib}/AnyData/Storage
%{perl_vendorlib}/AnyData/Storage/*.pm
%{_mandir}/man3/*
