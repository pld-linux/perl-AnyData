#
# Conditional build:
# _with_tests - perform "make test" (hangs with XML::Twig or HTML::TableExtract installed)
%include	/usr/lib/rpm/macros.perl
%define	pdir	AnyData
Summary:	AnyData -- easy access to data in many formats
Summary(pl):	AnyData -- ³atwy dostêp do danych w ró¿nych formatach
Name:		perl-%{pdir}
Version:	0.05
Release:	3
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/authors/id/J/JZ/JZUCKER/AnyData-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
%if %{?_with_test:1}%{!?_with_test:0}
BuildRequires:	perl(Data::Dumper)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(XML::Twig)' 'perl(HTML::TableExtract)'

%description
The AnyData modules provide simple and uniform access to data from
many sources -- perl arrays, local files, remote files retrievable via
http or ftp -- and in many formats including flat files (CSV, Fixed
Length, Tab Delimited, etc), standard format files (Web Logs, Passwd
files, etc.),  structured files (XML, HTML Tables) and binary files
with parseable headers (mp3s, jpgs, pngs, etc).

%description -l pl
Modu³y AnyData daj± prosty i ujednolicony dostêp do danych z wielu
¼róde³ - tablic perlowych, plików lokalnych, plików zdalnych
dostêpnych po http lub ftp - oraz w wielu formatach, w tym p³askich
plikach (CSV, z polami o sta³ej d³ugo¶ci, ograniczonych tabami itp.),
plikach o standardowych formatach (logi WWW, pliki passwd), plikach
strukturalnych (tabele XML, HTML) oraz plikach binarnych z
parsowalnymi nag³ówkami (mp3, jpg, png itp.).

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL
%{__make}
%{?_with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/*.pm
%{perl_sitelib}/%{pdir}
%{_mandir}/man3/*
