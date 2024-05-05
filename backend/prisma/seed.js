const { PrismaClient } = require('@prisma/client');

const prisma = new PrismaClient();

async function main() {
  await prisma.card.createMany({
    data: [
      {id: 1, name: 'barriere_chantier', rarity: 'common'},
      {id: 2, name: 'cable_iphone_casse', rarity: 'common'},
      {id: 3, name: 'chat_mignon', rarity: 'common'},
      {id: 4, name: 'esc_key', rarity: 'common'},
      {id: 5, name: 'extincteur', rarity: 'common'},
      {id: 6, name: 'latte_lit', rarity: 'common'},
      {id: 7, name: 'mcdo_toy', rarity: 'common'},
      {id: 8, name: 'panneau_routier', rarity: 'common'},
      {id: 9, name: 'plot_de_chantier', rarity: 'common'},
      {id: 10, name: 'pot_a_eau', rarity: 'common'},
      {id: 11, name: 'ressort', rarity: 'common'},
      {id: 12, name: 'rj45', rarity: 'common'},
      {id: 13, name: 'vaisselle_mcdo', rarity: 'common'},
      {id: 14, name: 'vis_chaise', rarity: 'common'}
    ],
  });

  console.log('Multiple rows created successfully');
}

main()
  .catch((e) => {
    throw e;
  })
  .finally(async () => {
    await prisma.$disconnect();
  });
