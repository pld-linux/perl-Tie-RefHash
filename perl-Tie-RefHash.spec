#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"

%define		pdir	Tie
%define		pnam	RefHash
%include	/usr/lib/rpm/macros.perl
Summary:	Tie::RefHash - use references as hash keys
Name:		perl-Tie-RefHash
Version:	1.39
Release:	2
# even cpan dont know license
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Tie/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	179d4d02924bd9716e2ffe585cbd36c8
URL:		http://search.cpan.org/dist/Tie-RefHash/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides the ability to use references as hash keys if you
first tie the hash variable to this module. Normally, only the keys of
the tied hash itself are preserved as references; to use references as
keys in hashes-of-hashes, use Tie::RefHash::Nestable, included as part
of Tie::RefHash.

It is implemented using the standard perl TIEHASH interface. Please
see the tie entry in perlfunc(1) and perltie(1) for more information.

The Nestable version works by looking for hash references being stored
and converting them to tied hashes so that they too can have
references as keys. This will happen without warning whenever you
store a reference to one of your own hashes in the tied hash.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/Tie/RefHash

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Tie/RefHash.pm
%dir %{perl_vendorlib}/Tie/RefHash
%{_mandir}/man3/Tie::RefHash.3pm*
