#!/usr/bin/python
#
# Title:       Important Security Announcement for tomcat6 SUSE-SU-2021:14705-1
# Description: Security fixes for SUSE Linux Enterprise 11 SP4 LTSS
# Source:      Security Announcement Parser v1.6.1
# Modified:    2021 May 04
#
##############################################################################
# Copyright (C) 2021 SUSE LLC
##############################################################################
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.
#
#  Authors/Contributors:
#   Jason Record <jason.record@suse.com>
#
##############################################################################

import os
import Core
import SUSE

META_CLASS = "Security"
META_CATEGORY = "SLE"
META_COMPONENT = "tomcat6"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2021-April/008669.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = True
NAME = 'tomcat6'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2021:14705-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 11):
	if ( SERVER['DistroPatchLevel'] == 4 ):
		PACKAGES = {
			'tomcat6': '6.0.53-0.57.19.1',
			'tomcat6-admin-webapps': '6.0.53-0.57.19.1',
			'tomcat6-docs-webapp': '6.0.53-0.57.19.1',
			'tomcat6-javadoc': '6.0.53-0.57.19.1',
			'tomcat6-jsp-2_1-api': '6.0.53-0.57.19.1',
			'tomcat6-lib': '6.0.53-0.57.19.1',
			'tomcat6-servlet-2_5-api': '6.0.53-0.57.19.1',
			'tomcat6-webapps': '6.0.53-0.57.19.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

