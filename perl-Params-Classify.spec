#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Params
%define		pnam	Classify
%include	/usr/lib/rpm/macros.perl
Summary:	Params::Classify - argument type classification
#Summary(pl.UTF-8):	
Name:		perl-Params-Classify
Version:	0.013
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Params/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	63d24fbec775472ada49d16bce4a9b1f
# generic URL, check or change before uncommenting
#URL:		http://search.cpan.org/dist/Params-Classify/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides various type-testing functions.  These are
intended for functions that, unlike most Perl code, care what type of
data they are operating on.  For example, some functions wish to
behave differently depending on the type of their arguments (like
overloaded functions in C++).

There are two flavours of function in this module.  Functions of the
first flavour only provide type classification, to allow code to
discriminate between argument types.  Functions of the second flavour
package up the most common type of type discrimination: checking that
an argument is of an expected type.  The functions come in matched
pairs, of the two flavours, and so the type enforcement functions
handle only the simplest requirements for arguments of the types
handled by the classification functions.  Enforcement of more complex
types may, of course, be built using the classification functions, or
it may be more convenient to use a module designed for the more
complex job, such as Params::Validate.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Params/*.pm
%dir %{perl_vendorarch}/auto/Params/Classify
%{perl_vendorarch}/auto/Params/Classify/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Params/Classify/*.so
%{_mandir}/man3/*
