#
# Conditional build:
%bcond_without	tests	# don't perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	AnyData
Summary:	AnyData - easy access to data in many formats
Summary(pl):	AnyData - ³atwy dostêp do danych w ró¿nych formatach
Name:		perl-AnyData
Version:	0.10
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/authors/id/J/JZ/JZUCKER/AnyData-%{version}.tar.gz
# Source0-md5:	ff9fb4c7d8b99d63a773e66f0ccba788
%if %{with tests}
BuildRequires:	perl-CGI
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(XML::Twig)' 'perl(HTML::TableExtract)'

%description
The AnyData modules provide simple and uniform access to data from
many sources - perl arrays, local files, remote files retrievable via
HTTP or FTP - and in many formats including flat files (CSV, Fixed
Length, Tab Delimited, etc), standard format files (Web Logs, Passwd
files, etc.),  structured files (XML, HTML Tables) and binary files
with parseable headers (mp3s, jpgs, pngs, etc).

%description -l pl
Modu³y AnyData daj± prosty i ujednolicony dostêp do danych z wielu
¼róde³ - tablic perlowych, plików lokalnych, plików zdalnych
dostêpnych po HTTP lub FTP - oraz w wielu formatach, w tym p³askich
plikach (CSV, z polami o sta³ej d³ugo¶ci, ograniczonych tabami itp.),
plikach o standardowych formatach (logi WWW, pliki passwd), plikach
strukturalnych (tabele XML, HTML) oraz plikach binarnych z
parsowalnymi nag³ówkami (mp3, jpg, png itp.).

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
