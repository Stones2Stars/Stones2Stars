// gameAI.cpp
#include "CvGameCoreDLL.h"

#include "FProfiler.h"

#include "CvGameAI.h"
#include "CvGlobals.h"
#include "CvGlobals.h"
#include "CvInfos.h"
#include "CvPlayerAI.h"
#include "CvTeamAI.h"

// Public Functions...

CvGameAI::CvGameAI()
{
	AI_reset();
}


CvGameAI::~CvGameAI()
{
	AI_uninit();
}


void CvGameAI::AI_init()
{
	AI_reset();

	//--------------------------------
	// Init other game data
}


void CvGameAI::AI_uninit()
{
}


void CvGameAI::AI_reset()
{
	AI_uninit();

	m_iPad = 0;

	CvUnitAI::AI_clearCaches();
}


void CvGameAI::AI_makeAssignWorkDirty()
{
	PROFILE_EXTRA_FUNC();
	int iI;

	for (iI = 0; iI < MAX_PLAYERS; iI++)
	{
		if (GET_PLAYER((PlayerTypes)iI).isAlive())
		{
			GET_PLAYER((PlayerTypes)iI).AI_makeAssignWorkDirty();
		}
	}
}


void CvGameAI::AI_updateAssignWork()
{
	PROFILE_FUNC();

	int iI;

	for (iI = 0; iI < MAX_PLAYERS; iI++)
	{
		CvPlayer& kLoopPlayer = GET_PLAYER((PlayerTypes)iI);
		if (GET_TEAM(kLoopPlayer.getTeam()).isHuman() && kLoopPlayer.isAlive())
		{
			kLoopPlayer.AI_updateAssignWork();
		}
	}
}


int CvGameAI::AI_combatValue(const UnitTypes eUnit) const
{
	int iValue = 100;
	const CvUnitInfo& unit = GC.getUnitInfo(eUnit);

	if (unit.getDomainType() == DOMAIN_AIR)
	{
		iValue *= unit.getAirCombat();
	}
	else
	{
		iValue *= unit.getCombat();
		//TB Combat Mods Begin
		// Inactive
		//iValue += (((100 + unit.getArmor())/100)/5);
		//iValue += (((100 + unit.getPuncture())/100)/5);
		// Inactive END

		// TOOD: rethink these calculations
		//iValue += (((100 * unit.getPrecisionModifier())/100)/5);
		//iValue += (((100 * unit.getDodgeModifier())/100)/5);
		//iValue += (((100 * unit.getDamageModifier())/100)/5);
		//TB Combat Mods End

		iValue *= 100 + (2 * unit.getFirstStrikes() + unit.getChanceFirstStrikes()) * GC.getCOMBAT_DAMAGE() / 5;
		iValue /= 100;
	}

	iValue /= getBestLandUnitCombat();

	return iValue;
}


void CvGameAI::read(FDataStreamBase* pStream)
{
	CvGame::read(pStream);

	pStream->Read(&m_iPad);
}


void CvGameAI::write(FDataStreamBase* pStream)
{
	CvGame::write(pStream);

	pStream->Write(m_iPad);
}

// Protected Functions...

// Private Functions...
