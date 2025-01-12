Summary:	Kerberos v5 PAM module
Name:		pam-krb5
Version:	4.11
Release:	2
License:	LGPLv2
Group:		System/Libraries
Url:		https://www.eyrie.org/~eagle/software/pam-krb5/
Source0:	http://archives.eyrie.org/software/kerberos/%{name}-%{version}.tar.gz
BuildRequires:	krb5-devel
BuildRequires:	pam-devel
BuildRequires:	pkgconfig(com_err)
Conflicts:	pam_krb5

%description
pam-krb5 provides a Kerberos v5 PAM module that supports authentication, user
ticket cache handling, simple authorization (via .k5login or checking Kerberos
principals against local usernames), and password changing. It can be
configured through either options in the PAM configuration itself or through
entries in the system krb5.conf file, and it tries to work around PAM
implementation flaws in commonly-used PAM-enabled applications such as OpenSSH
and xdm. 

%prep
%autosetup -p1

%build
%configure --libdir=/%{_lib}
%make_build

%install
%make_install

%files
%doc LICENSE NEWS README TODO
/%{_lib}/security/*
%{_mandir}/man5/pam_krb5.5*

