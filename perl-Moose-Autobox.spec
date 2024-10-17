%define upstream_name    Moose-Autobox
%define upstream_version 0.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	The Indexed role
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Moose/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(autobox)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Perl6::Junction)
BuildRequires:	perl(Test::Exception)
BuildArch:	noarch
Requires:	perl(autobox)

%description
Moose::Autobox provides an implementation of SCALAR, ARRAY, HASH & CODE for
use with the autobox manpage. It does this using a hierarchy of roles in a
manner similar to what Perl 6 _might_ do. This module, like the Class::MOP
manpage and the Moose manpage, was inspired by my work on the Perl 6 Object
Space, and the 'core types' implemented there.

A quick word about autobox
    The the autobox manpage module provides the ability for calling
    'methods' on normal Perl values like Scalars, Arrays, Hashes and Code
    references. This gives the illusion that Perl's types are first-class
    objects. However, this is only an illusion, albeit a very nice one. I
    created this module because the autobox manpage itself does not
    actually provide an implementation for the Perl types but instead only
    provides the 'hooks' for others to add implementation too.

Is this for real? or just play?
    Several people are using this module in serious applications and it
    seems to be quite stable. The underlying technologies of the autobox
    manpage and the Moose::Role manpage are also considered stable. There
    is some performance hit, but as I am fond of saying, nothing in life is
    free. If you have any questions regarding this module, either email me,
    or stop by #moose on irc.perl.org and ask around.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.110.0-2mdv2011.0
+ Revision: 655060
- rebuild for updated spec-helper

* Mon Apr 26 2010 Jérôme Quelin <jquelin@mandriva.org> 0.110.0-1mdv2011.0
+ Revision: 539086
- update to 0.11

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-1mdv2010.1
+ Revision: 460764
- update to 0.10

* Sun Jun 07 2009 Jérôme Quelin <jquelin@mandriva.org> 0.90.0-2mdv2010.0
+ Revision: 383744
- adding missing provides: stripped by rpm

* Fri May 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.90.0-1mdv2010.0
+ Revision: 381061
- adding missing buildrequires:
- adding missing buildrequires:
- import perl-Moose-Autobox


* Fri May 29 2009 cpan2dist 0.09-1mdv
- initial mdv release, generated with cpan2dist

