%define name	scramble
%define version 4.5.0
%define release %mkrel 8

Name: 	 	%{name}
Summary: 	File encryption utility used by xffm
Version: 	%{version}
Release: 	%{release}

Source:		http://downloads.sourceforge.net/xffm/%{name}-%{version}.tar.bz2
URL:		http://xffm.sf.net
License:	GPL
Group:		Graphical desktop/Other
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	xfce-dev-tools
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	glib-gettextize 

%description
Scramble is the command find tool used by the Xffm-filemanager to 
encrypt and descrypt files upon user request. The application is 
also used to schred files before deleting.

%prep
%setup -q

%build
autoreconf -fi -I /usr/share/xfce4/dev-tools/m4macros
%configure2_5x
%make
										
%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING* ChangeLog NEWS* README*
%{_bindir}/%{name}
%{_bindir}/unscramble
%{_mandir}/man1/*
%{_datadir}/xffm/%{name}
%{_libdir}/pkgconfig/%{name}.pc
