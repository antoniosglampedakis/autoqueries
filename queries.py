tagsquery = \
'''select ec.FestivalYear,  ec.FestivalCode, ec.EntryTypeName as Award, ec.MediaDescription, ec.CategoryDescription as "Category Description",
ED.Advertiser, ED.short as Shortlist, ed.EntryId as "All Entries", ed.Product,ed.title,
ED.AwardCountCode as Winner, ED.PrizeCode, ED.CategoryCode as "Cat Code",  ed.CategorySubTypeID, ed.CatalogueNo,
cd.CompanyName, CD.NetworkCode, cd.NetworkName, CD.UltimateHoldingCompanyName,  
cd.Country, cd.GroupCompanyName, cd.coTown, cd.CompanyType, cd.RegionName,

sec.Sector_Name sector_name,
subSec.Sector_Name sub_sector_name
,
tgg.Name as taggroupgroupname,
tg.Name TagGroupName,
t.Name tagname

from PublishedArchiveEntryData pED

inner Join ArchiveCompanyData as CD
	on pED.EntrantCompanyNo = CD.companyNo 
	and ped.Festivalyear = cd.ArchiveYear

inner join ArchiveEntryData ed
	on ed.EntryId = ped.entryid
	and ed.FestivalYear = ped.FestivalYear
	and ed.FestivalCode = ped.FestivalCode  COLLATE Latin1_General_CI_AI

left join ArchiveEntryCategories ec

	ON ec.FestivalCode = ped.FestivalCode COLLATE Latin1_General_CI_AI
	AND ec.FestivalYear = ped.FestivalYear
	AND ec.CategoryCode = ped.CategoryCode COLLATE Latin1_General_CI_AI
	AND ec.EntryTypeId = ped.EntryTypeId

left JOIN IAFF.DBO.ArchiveCampaignTags et 
	ON ped.FestivalYear = et.FestivalYear
	AND ped.FestivalCode = et.FestivalCode COLLATE Latin1_General_CI_AI
	AND ped.EntryId = et.EntryID

left JOIN IAFF.DBO.ArchiveTags t WITH (NOLOCK)
	ON et.TagID = t.TagId 
	AND et.FestivalCode  = t.FestivalCode 
	AND et.FestivalYear = t.FestivalYear 

left JOIN IAFF.DBO.ArchiveTagGroups tg WITH (NOLOCK)
	ON t.TagGroupID = tg.TagGroupID
	AND t.FestivalCode  = tg.FestivalCode 
	AND t.FestivalYear = tg.FestivalYear 
left join ArchiveTagGroupGroups tgg
    on tgg.TagGroupGroupID = tg.TagGroupGroupId
    and tgg.FestivalCode = tg.FestivalCode
    and tgg.FestivalYear = tg.FestivalYear

LEFT JOIN 
ArchiveEntrySector sec
	ON sec.FestivalYear = ed.FestivalYear
	AND sec.FestivalCode = ed.FestivalCode COLLATE SQL_Latin1_General_CP1_CI_AS 
	AND sec.Sector_ID = ed.sector_id
LEFT JOIN ArchiveEntrySector subSec
	ON subSec.FestivalYear = ed.FestivalYear
	AND subSec.FestivalCode = ed.FestivalCode COLLATE SQL_Latin1_General_CP1_CI_AS 
	AND subSec.Sector_ID = ed.sector_sub_id 	

Where
ed.FestivalCode in {}
and ped.FestivalYear >= {}
and ped.FestivalYEar <={}
and ped.Cancelled <> 1
'''


notTagsQuery = tagsquery = \
'''select ed.FestivalYear,  ec.FestivalCode, ec.EntryTypeName as Award, ec.MediaDescription, ec.CategoryDescription as "Category Description",
ED.Advertiser, ED.short as Shortlist,  ed.EntryId as "All Entries",ed.Product, ed.title,
ED.AwardCountCode as Winner, ED.PrizeCode, ED.CategoryCode as "Cat Code",  ed.CategorySubTypeID, ed.CatalogueNo,
cd.CompanyName, CD.NetworkCode, cd.NetworkName, CD.UltimateHoldingCompanyName,  
cd.Country, cd.GroupCompanyName, cd.coTown, cd.CompanyType, cd.RegionName,

sec.Sector_Name sector_name,
subSec.Sector_Name sub_sector_name

from PublishedArchiveEntryData pED

inner Join ArchiveCompanyData as CD
	on pED.EntrantCompanyNo = CD.companyNo 
	and ped.Festivalyear = cd.ArchiveYear

inner join ArchiveEntryData ed
	on ed.EntryId = ped.entryid
	and ed.FestivalYear = ped.FestivalYear
	and ed.FestivalCode = ped.FestivalCode  COLLATE Latin1_General_CI_AI

left join ArchiveEntryCategories ec

	ON ec.FestivalCode = ped.FestivalCode COLLATE Latin1_General_CI_AI
	AND ec.FestivalYear = ped.FestivalYear
	AND ec.CategoryCode = ped.CategoryCode COLLATE Latin1_General_CI_AI
	AND ec.EntryTypeId = ped.EntryTypeId



LEFT JOIN 
ArchiveEntrySector sec
	ON sec.FestivalYear = ed.FestivalYear
	AND sec.FestivalCode = ed.FestivalCode COLLATE SQL_Latin1_General_CP1_CI_AS 
	AND sec.Sector_ID = ed.sector_id
LEFT JOIN ArchiveEntrySector subSec
	ON subSec.FestivalYear = ed.FestivalYear
	AND subSec.FestivalCode = ed.FestivalCode COLLATE SQL_Latin1_General_CP1_CI_AS 
	AND subSec.Sector_ID = ed.sector_sub_id 	

Where
ed.FestivalCode in {}
and ped.FestivalYear >= {}
and ped.FestivalYEar <={}
and ped.Cancelled <> 1

'''


