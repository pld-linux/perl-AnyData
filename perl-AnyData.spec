#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	AnyData
Summary:	AnyData -- easy access to data in many formats
Summary(pl):	AnyData -- �atwy dost�p do danych w r�nych formatach
Name:		perl-%{pdir}
Version:	0.05
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
%if %{?_without_test:0}%{!?_without_test:1}
BuildRequires:	perl(Data::Dumper)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The AnyData modules provide simple and uniform access to data from many
sources -- perl arrays, local files, remote files retrievable via http
or ftp -- and in many formats including flat files (CSV, Fixed Length,
Tab Delimited, etc), standard format files (Web Logs, Passwd files,
etc.),  structured files (XML, HTML Tables) and binary files with
parseable headers (mp3s, jpgs, pngs, etc).

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{version}

%build
perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

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
