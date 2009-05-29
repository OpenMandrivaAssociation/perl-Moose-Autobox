%define upstream_name    Moose-Autobox
%define upstream_version 0.09

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    The Indexed role
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Moose/%{upstream_name}-%{upstream_version}.tar.gz


BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


