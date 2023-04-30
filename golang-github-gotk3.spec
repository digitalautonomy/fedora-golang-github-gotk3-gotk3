# Generated by go2rpm 1
%bcond_without check

# https://github.com/gotk3/gotk3
%global goipath         github.com/gotk3/gotk3
Version:                0.6.2

%gometa

%global common_description %{expand:
Go bindings for GTK3.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTIONS.md README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Go bindings for GTK3

License:        ISC
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
Xvfb :99 &
export DISPLAY=:99
%gocheck
%endif

%gopkgfiles

%changelog
* Sat Apr 29 13:00:00 -05 2023 CAD <fedora@autonomia.digital> 0.0.1-1
- Update to new version

* Mon Mar 16 11:46:50 -05 2020 rafael <rafael@autonomia.digital> - 0.4.0-1
- Initial package
