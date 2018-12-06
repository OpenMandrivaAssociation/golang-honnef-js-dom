# Run tests in check section
%bcond_without check

%global goipath         honnef.co/go/js/dom
%global forgeurl        https://github.com/dominikh/go-js-dom
%global commit          6da835bec70f84cd4f0c0b8a7239a9260b6bc37f

%global common_description %{expand:
GopherJS bindings for the JavaScript DOM APIs.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        GopherJS bindings for the JavaScript DOM APIs
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/gopherjs/gopherjs/js)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git6da835b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180420git6da835b
- First package for Fedora

