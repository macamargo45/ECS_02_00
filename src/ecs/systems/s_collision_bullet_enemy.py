import esper
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.tags.c_tag_bullet import CTagBullet
from src.ecs.components.tags.c_tag_enemy import CTagEnemy


def system_collision_bullet_enemy(word: esper.World):

    components_enemys = word.get_components(CSurface, CTransform, CTagEnemy)
    components_bullets = word.get_components(CSurface, CTransform, CTagBullet)

    for enemy_entity, (c_s, c_t, _) in components_enemys:

        enemy_rect = c_s.surf.get_rect(topleft=c_t.pos)

        for bullet_entity, (cb_s, cb_t, _) in components_bullets:
            bullet_rect = cb_s.surf.get_rect(topleft=cb_t.pos)
            if enemy_rect.colliderect(bullet_rect):
                word.delete_entity(enemy_entity)
                word.delete_entity(bullet_entity)
