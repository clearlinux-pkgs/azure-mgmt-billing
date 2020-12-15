#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : azure-mgmt-billing
Version  : 0.2.0
Release  : 9
URL      : https://files.pythonhosted.org/packages/24/35/3b9da47363a300203c324b572a1ae3c096dc031905d582d5a27bd59a8d4e/azure-mgmt-billing-0.2.0.zip
Source0  : https://files.pythonhosted.org/packages/24/35/3b9da47363a300203c324b572a1ae3c096dc031905d582d5a27bd59a8d4e/azure-mgmt-billing-0.2.0.zip
Summary  : Microsoft Azure Billing Client Library for Python
Group    : Development/Tools
License  : MIT
Requires: azure-mgmt-billing-python = %{version}-%{release}
Requires: azure-mgmt-billing-python3 = %{version}-%{release}
Requires: azure-common
Requires: msrestazure
BuildRequires : azure-common
BuildRequires : buildreq-distutils3
BuildRequires : msrestazure

%description
==============================
        
        This is the Microsoft Azure Billing Client Library.
        
        Azure Resource Manager (ARM) is the next generation of management APIs that
        replace the old Azure Service Management (ASM).
        
        This package has been tested with Python 2.7, 3.4, 3.5 and 3.6.
        
        For the older Azure Service Management (ASM) libraries, see

%package python
Summary: python components for the azure-mgmt-billing package.
Group: Default
Requires: azure-mgmt-billing-python3 = %{version}-%{release}

%description python
python components for the azure-mgmt-billing package.


%package python3
Summary: python3 components for the azure-mgmt-billing package.
Group: Default
Requires: python3-core
Provides: pypi(azure_mgmt_billing)
Requires: pypi(azure_common)
Requires: pypi(azure_mgmt_nspkg)
Requires: pypi(msrestazure)

%description python3
python3 components for the azure-mgmt-billing package.


%prep
%setup -q -n azure-mgmt-billing-0.2.0
cd %{_builddir}/azure-mgmt-billing-0.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588788669
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## Remove excluded files
rm -f %{buildroot}/usr/lib/python3.8/site-packages/azure/__init__.py
rm -f %{buildroot}/usr/lib/python3.8/site-packages/azure/__pycache__/__init__.cpython-38.pyc
rm -f %{buildroot}/usr/lib/python3.8/site-packages/azure/mgmt/__init__.py
rm -f %{buildroot}/usr/lib/python3.8/site-packages/azure/mgmt/__pycache__/__init__.cpython-38.pyc

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
