#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Params
%define		pnam	Classify
Summary:	Params::Classify - argument type classification
Summary(pl.UTF-8):	Params::Classify - klasyfikacja typu argumentu
Name:		perl-Params-Classify
Version:	0.015
Release:	7
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Params/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3c3367d759ed5bd6fe86c1f35e9b51ed
URL:		https://metacpan.org/dist/Params-Classify
BuildRequires:	perl-ExtUtils-ParseXS >= 2.2006
BuildRequires:	perl-Module-Build >= 0.33
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Scalar-List-Utils >= 1.01
BuildRequires:	perl-Test-Simple
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides various type-testing functions. These are
intended for functions that, unlike most Perl code, care what type of
data they are operating on. For example, some functions wish to
behave differently depending on the type of their arguments (like
overloaded functions in C++).

%description -l pl.UTF-8
Ten moduł udostępnia różne funkcje do sprawdzania typów. Mają być
przydatne dla funkcji, które - w przeciwieństwie do większości kodu
perlowego - zwracają uwagę na typ danych, na których operują; np.
dla funkcji, które zachowują się różnie w zależności od typu
argumentów (jak przeciążone funkcje w C++).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	installdirs=vendor \
	--config cc="%{__cc}" \
	--config ld="%{__cc}" \
	--config optimize="%{rpmcflags}"

./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install \
	destdir=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Params/Classify/Classify.bs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Params/Classify.pm
%dir %{perl_vendorarch}/auto/Params/Classify
%attr(755,root,root) %{perl_vendorarch}/auto/Params/Classify/Classify.so
%{_mandir}/man3/Params::Classify.3pm*
