%define		pkg	mkdirp
Summary:	Recursively mkdir, like "mkdir -p"
Name:		nodejs-%{pkg}
Version:	0.3.4
Release:	1
License:	MIT
Group:		Development/Libraries
URL:		https://github.com/substack/node-mkdirp
Source0:	http://registry.npmjs.org/mkdirp/-/%{pkg}-%{version}.tgz
# Source0-md5:	8dd299eb49e17f94e145292040998f32
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Recursively mkdir, like "mkdir -p".

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -pr index.js package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.markdown
%{nodejs_libdir}/%{pkg}
%{_examplesdir}/%{name}-%{version}
